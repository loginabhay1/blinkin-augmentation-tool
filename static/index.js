var blob_value;

function showImage(src, target) {
            var fr = new FileReader();

             fr.onload = function(){
      target.src = fr.result;
      blob_value = fr.result.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
      // console.log("[INFO] Blob Value : ", blob_value);
      var payload1 = {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      body: blob_value
      };
      // TODO: Change other AJAX calls to fetch calls.
      var response = fetch("http://127.0.0.1:7001/aug_url", payload1)
      .then(function (response) {
        return response.text();
      })
      .then(function (text) {
        console.log("[INFO] Result : ", text)
        document.getElementById("success").innerHTML = text.fontcolor("red");
      })
    }
           fr.readAsDataURL(src.files[0]);

        }
        function putImage() {
            var src = document.getElementById("select_image");
            var target = document.getElementById("target");
            showImage(src, target);
        }