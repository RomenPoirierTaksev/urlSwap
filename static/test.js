let button = document.getElementById('go-button');
var popup = document.getElementById("myPopup");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

function swapUrl(){
    let url = document.getElementById('url').value;
    popup.classList.toggle("hidden");
    fetch('/swapUrl', {

        // Declare what type of data we're sending
        headers: {
          'Content-Type': 'application/json'
        },
    
        // Specify the method
        method: 'POST',
    
        // A JSON payload
        body: JSON.stringify(
            url
        )
    }).then(function (response) { // At this point, Flask has printed our JSON
        if(response.status == 500){
            return response.status;
        }
        return response.text();
    }).then(async function (text) {
        if(text == 500){
            document.getElementById("output").innerHTML = "Unable to find song";
        }else{
            if(text == "Invalid URL"){
                document.getElementById("output").innerHTML = text;
            }else{
                document.getElementById("output").innerHTML = "New URL: " + text;
                navigator.clipboard.writeText(text).then(function() {
                    console.log('Async: Copying to clipboard was successful!');
                  }, function(err) {
                    console.error('Async: Could not copy text: ', err);
                  });
                popup.classList.toggle("show");
                await sleep(2000);
                popup.classList.toggle("hideAnimation");
                await sleep(1000);
                popup.classList.toggle("hide")

            }
            
            
        }
    });
}

button.addEventListener("click", swapUrl);