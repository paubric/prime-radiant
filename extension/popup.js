document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  var resultsLabel = document.getElementById('results');
  checkPageButton.addEventListener('click', function() {

    chrome.tabs.getSelected(null, function(tab) {
      var url = 'http://127.0.0.1:5000/scan';
      var data = {url:tab.url};

      fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers:{
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .then(response => {
          alert(JSON.stringify(response));
          resultsLabel.textContent = 'Subjectivity: ' + response['sub'];
        })
      .catch(error => alert('Error:', error));

    });
  }, false);
}, false);
