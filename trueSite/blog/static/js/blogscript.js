function textWithPictures(text){
    var pathesStart = text.indexOf('~^');
    var imagesPathes = text.slice(pathesStart + 2);
    var textBody = text.slice(0, pathesStart);
    var pathesArr = imagesPathes.split(',');
    pathesArr.pop();
    var imageIndex = 0;
    while(textBody.length > 1){
        imageIndex = textBody.indexOf('?img?');
        if(imageIndex == -1){
            var splitedText = textBody.split('<br>');
            for(var i = 1; i < splitedText.length; i++){
                var tempParagraph = document.createElement('p');
                tempParagraph.innerHTML = splitedText[i];
                document.getElementById("content-pictures").appendChild(tempParagraph);
                var tempSep = document.createElement('hr');
                tempSep.className = 'separator';
                document.getElementById("content-pictures").appendChild(tempSep);
            }
            break;
        }
        else{
        var newPar = document.createElement("p");
        newPar.innerHTML = textBody.slice(0, imageIndex);
           
        }
        imageIndex = imageIndex + 5;
        if(imageIndex < textBody.length - 1){
            textBody = textBody.slice(imageIndex);
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
    }

}