function textWithPictures(text){
    var pathesStart = text.indexOf('~^');
    var imagesPathes = text.slice(pathesStart + 2);
    var textBody = text.slice(0, pathesStart);
    var pathesArr = imagesPathes.split(',');
    pathesArr.pop();
    var enterIndex = 0;
    while(textBody.length > 1){
        enterIndex = textBody.indexOf('{%nl}');
        if(enterIndex == -1){
            var noBreaks = document.createElement("p");
            noBreaks.innerHTML = textBody;
            document.getElementById("content-pictures").appendChild(noBreaks);
            for(var i = 0; i < pathesArr.length; i++){
                var tempImg = document.createElement("img");
                tempImg.src = pathesArr[i];
                document.getElementById("content-pictures").appendChild(tempImg);
            }
            break;
        }
        else{
         var newPar = document.createElement("p");
        newPar.innerHTML = textBody.slice(0, enterIndex);
           
        }
        enterIndex = enterIndex + 5;
        if(enterIndex < textBody.length - 1){
            textBody = textBody.slice(enterIndex);
        }
        else{
            break;
        }
        document.getElementById("content-pictures").appendChild(newPar);
        if(pathesArr.length != 0)
        {
            var imgPar = document.createElement("p");
            var img = document.createElement("img");
            img.src = pathesArr.shift();
            imgPar.appendChild(img);
            document.getElementById("content-pictures").appendChild(imgPar);
        }
        else{
            var separator = document.createElement("hr");
            separator.className = "separator";
            document.getElementById("content-pictures").appendChild(separator);
        }
    }

}