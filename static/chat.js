var me = {};
//me.avatar = "https://lh6.googleusercontent.com/-lr2nyjhhjXw/AAAAAAAAAAI/AAAAAAAARmE/MdtfUmC0M4s/photo.jpg?sz=48";
me.avatar = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png"


var you = {};
you.avatar = "http://www.cleverbot.com/images/cleverbot226x94.jpg";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}

//-- No use time. It is a javaScript effect.

/*function insertChat(who, text, time = 0){
var control = "";
var date = formatAMPM(new Date());

if (who == "me"){
console.log("something is starting");
control = '<li style="width:100%">' +
'<div class="msj macro">' +
'<div class="avatar"><img class="img-circle" style="width:100%;" src="'+ me.avatar +'" /></div>' +
'<div class="text text-l">' +
'<p>'+ text +'</p>' +
'<p><small>'+date+'</small></p>' +
'</div>' +
'</div>' +
'</li>';
}else{
control = '<li style="width:100%;">' +
'<div class="msj-rta macro">' +
'<div class="text text-r">' +
'<p>'+text+'</p>' +
'<p><small>'+date+'</small></p>' +
'</div>' +
'<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%;" src="'+you.avatar+'" /></div>' +
'</li>';
}
console.log('something is continuing');
//setTimeout(
//    function(){
console.log(control);
$("ul").append(control);
console.log('yay?');
//    }, time);
console.log("something is ending");
}*/

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keyup", function(e){
    alert(e.which);
    if (e.which == 13){
        var text = $(this).val();
        if (text !== ""){
            insertChat("me", text);
            $(this).val('');
        }
    }
});

//-- Clear Chat
resetChat();

//-- Print Messages
//insertChat("me", "Hello Tom...", 0);
/*insertChat("you", "Hi, Pablo", 1500);
insertChat("me", "What would you like to talk about today?", 3500);
insertChat("you", "Tell me a joke",7000);
insertChat("me", "Spaceman: Computer! Computer! Do we bring battery?!", 9500);
insertChat("you", "LOL", 12000);*/


//-- NOTE: No use time on insertChat.
$( document ).ready(function() {
    //All jquery has to be here because flask is special
    $(".mytext").on("keyup", function(e){
        if (e.which == 13){
            var text = $(this).val();
            if (text !== ""){
                insertChat("me", text);
                //console.log(text);
                $(this).val('');
                var ret = cleverbot(text);
                console.log(ret);
                //insertChat("cleverbot", ret, 100); //You can change cleverbot's delay with this.
            }
        }

    });
    function cleverbot(i) {
        var aj = $.ajax({
            type: "POST",
            url: "/clever",
            async: true,
            data: { input: i },
            beforeSend: function() {
                console.log('before');
            },
            success: function(result) {
                console.log(result);
                //insertChat("me", aj.responseText,0);
                insertChat("cleverbot", result, 0);
            }
        });
        console.log("done");
        //insertChat("cleverbot", aj.responseText, 100);
        return aj.responseText;
    }

    function resetChat(){
        $("ul").empty();
    }
    function insertChat(who, text, time = 0){
        var control = "";
        var date = formatAMPM(new Date());

        if (who == "me"){
            //console.log("something is starting");
            control = '<li style="width:100%">' +
            '<div class="msj macro">' +
            '<div class="avatar"><img class="img-circle" style="width:100%;" src="'+ me.avatar +'" /></div>' +
            '<div class="text text-l">' +
            '<p>'+ text +'</p>' +
            '<p><small>'+date+'</small></p>' +
            '</div>' +
            '</div>' +
            '</li>';
        }else{
            control = '<li style="width:100%;">' +
            '<div class="msj-rta macro">' +
            '<div class="text text-r">' +
            '<p>'+text+'</p>' +
            '<p><small>'+date+'</small></p>' +
            '</div>' +
            '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%;" src="'+you.avatar+'" /></div>' +
            '</li>';
        }
        //console.log('something is continuing');
        setTimeout(
            function(){
        //console.log(control);
        $("ul").append(control);
        //document.
        //console.log('yay?');
            }, time);
        //console.log("something is ending");
    }
});
