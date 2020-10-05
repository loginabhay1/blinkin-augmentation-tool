var blob_value;
var fileListDisplay = document.getElementById('file-list-display');
var fileList = [];
var success_text = '';
var count = 0;

function showImage(file_value, target, len) {
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
                  var response = fetch("http://127.0.0.1:7001/aug_url", payload1)
                  .then(function (response) {
                    return response.text();
                  })
                  .then(function (text) {
                    console.log("[INFO] Result : ", text);
                    count++;
                    success_text = text;
                    if (count % len == 0) {
                      document.getElementById("success").innerHTML = success_text.fontcolor("red");
                    }
                  })
            }
            fr.readAsDataURL(file_value);

        }

function renderFileList(){
    fileListDisplay.innerHTML = '';
    fileList.forEach(function (file, index) {
      var fileDisplayEl = document.createElement('p');
      fileDisplayEl.innerHTML = (index + 1) + ': ' + file.name.bold();
      fileListDisplay.appendChild(fileDisplayEl);
    });
}

function putImage() {
    var src = document.getElementById("select_image");
    var target = document.getElementById("target");
    fileList = [];
    for (var i = 0; i < src.files.length; i++) {
          fileList.push(src.files[i]);
    }
    console.log(fileList);
    renderFileList();
    let len = src.files.length;
    for (var i = 0; i < src.files.length; i++) {
      showImage(src.files[i], target, len);
    }
}