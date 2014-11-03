function PsyTestModel(paper_data) {
    var self = this;

    function showQuestionIndex(index) {
				if (! paper_data.questions) return;
				var q = paper_data.questions[index];
				self.question(q.text);
				self.options(q.options);
				self.index = index;
				self.data = q;
    }

    function showQuestionId(id) {
				for (var i = 0; i < paper_data.questions.length; i += 1) {
						var q = paper_data.questions[i];
						if (q.id === id) {
								showQuestionIndex(i);
						}
				}
    }

    function pushOptionItem(idx, score) {
				self.score(self.score() + score);
				self.history.push({idx:idx, score:score});
    }
    
    function popOptionItem() {
				var item = self.history.pop();
				self.score(self.score() - item.score);
				showQuestionIndex(item.idx);
    }

    function showResult() {
				self.isEnd(true);
				console.log(self.score());
				for (var i = 0; i < paper_data.results.length; i += 1) {
						var r = paper_data.results[i];
						var score = self.score();
						if (score >= r.score_begin && score < r.score_end) {
								self.result(r.text); break;
						}
				}
    }
    
    self.isEnd = ko.observable(false);
    self.question = ko.observable();
    self.options = ko.observableArray();
    self.history = ko.observableArray();
    self.score = ko.observable(0);
    self.result = ko.observable();
    
    self.clickOption = function(data, event) {
				pushOptionItem(self.index, data.score);
				if (data.show_result || 
						self.index + 1 == paper_data.questions.length) {
						showResult();
						return;
				}
				if (data.next) {
						showQuestionId(data.next);
				} else {
						showQuestionIndex(self.index + 1);
				}
    }

    self.clickUndo = function(data, event) {
				popOptionItem();
    }

    showQuestionIndex(0);
}

