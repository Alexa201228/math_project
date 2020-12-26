window.onload = onLoadSize();
$(window).resize(controlSize);


function onLoadSize(){
    controlSize();
}


function controlSize(){
    if($(window).width() <= 650){
        smallScreen();
    }
    else{
        bigScreen();
    }
}
function bigScreen(){

    $("#return-to-top").css('max-width', '50px');
    $("#return-to-top").css('max-heigth', '50px');
    $("#return-to-top i").css('top', "13px");
    $("#return-to-top i").css('left', "16px");
    $("#return-to-top i").css('font-size', "19px");
}

function smallScreen(){
        $("#return-to-top").css('max-width', '20px');
        $("#return-to-top").css('max-heigth', '20px');
        $("#return-to-top i").css('top', "4px");
        $("#return-to-top i").css('left', "4px");
        $("#return-to-top i").css('font-size', "14px");
}