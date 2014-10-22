function ChatroomModule(pollUrl, sendUrl) {
		this.username = ko.observable();
    this.receiver = ko.observable();
    this.message = ko.observable();
    this.messageList = ko.observableArray();
    this.isSending = ko.observable(false);
    this.receiverId = ko.observable(0);
    this.pollUrl = pollUrl;
    this.sendUrl = sendUrl;
		this.partId = 0;
    
    var self = this;
    this.clickReceiver = function(data, event) {
        if (!data.source) return;
        self.putReceiver(data.source, data.name);
    };

		this.clickSendBtn = function(data, event) {
				self.sendMessage();
		};
		this.clickCleanBtn = function(data, event) {
				self.messageList([]);
		}
    
}
(function(Class) {
    Class.prototype.putReceiver = function(id, username) {
				this.receiverId(id);
				this.receiver(username);
    };

    Class.prototype.sendMessage = function() {
				this.isSending(true);
        var self = this;
        var csrf = $.cookie("csrftoken");
        var message = this.message();
        $.post(self.sendUrl, {
            csrfmiddlewaretoken:csrf,
            message:message,
            target:this.receiverId()
        }, function(data) {
            if (!data.error) {
								data['source'] = 0;
                //self.messageList.push({id:data.id, message:message, name:""});
								self.messageList.push(data);
            }
            self.message("");
            self.isSending(false);
        }, "json");
    };

    Class.prototype.pollMessage = function() {
        var self = this;
        var csrf = $.cookie("csrftoken");
				var data = {csrfmiddlewaretoken:csrf};
				if (this.partId) data['id'] = this.partId;
        $.post(self.pollUrl, data, function(data) {
						var list = data.data;
						self.username(data.name);
            for (var i = 0; i < list.length; i += 1) {
                var m = list[i];
                self.messageList.push(m);
            }
        }, "json");
    };

})(ChatroomModule);

