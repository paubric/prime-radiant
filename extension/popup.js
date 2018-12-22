document.addEventListener('DOMContentLoaded', function() {
  var subLabel = document.getElementById('subLabel');
  var polLabel = document.getElementById('polLabel');
  var subBar = document.getElementById('subBar');
  var polBar = document.getElementById('polBar');
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
          subLabel.textContent = 'Subjectivity: ' + response['sub'];
          subBar.value = response['sub'];
          var newPol = ((parseFloat(response['pol'])+1)/2).toString();
          polLabel.textContent = 'Polarity: ' + newPol;
          polBar.value = newPol;
        })
      .catch(error => alert('Error:', error));

    });
}, false);
