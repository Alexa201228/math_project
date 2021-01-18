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
            var tempPar = document.createElement('p');
            tempPar.innerHTML = textBody;
            document.getElementById("content-pictures").appendChild(tempPar) ;
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
            var img = document.createElement("img");
            img.src = pathesArr.shift();
            document.getElementById("content-pictures").appendChild(img);
        }
        var temp = document.getElementsByTagName('p');
        for(var i = 2; i < temp.length; i++){
            temp[i].innerHTML = temp[i].innerText
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
		    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
		    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
		    .replace(/^\\qt (.*$)/gim, '<blockquote>$1</blockquote>')
		    .replace(/\*\*(.*)\*\*/gim, '<b>$1</b>')
		    .replace(/\*(.*)\*/gim, '<i>$1</i>')
		    .replace(/\[(.*?)\]\((.*?)\)/gim, "<a href='$2'>$1</a>")
            .replace(/^\l(.*$)/gim, '<br/><hr/>$1');
    } 
    }

}