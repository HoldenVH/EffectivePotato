var me = {};
//me.avatar = "https://lh6.googleusercontent.com/-lr2nyjhhjXw/AAAAAAAAAAI/AAAAAAAARmE/MdtfUmC0M4s/photo.jpg?sz=48";
me.avatar = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png"


var you = {};
you.avatar = "http://www.cleverbot.com/images/cleverbot226x94.jpg";

var lastClever = "";

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
    $("#pclick").click(function() {
        cprompt();
    });
    $(".mytext").on("keyup", function(e){
        if (e.which == 13){
            var text = $(this).val();
            if (text !== ""){
                insertChat("me", text);
                $(this).val('');
                var ret = cleverbot(text, "cleverbot");
            }
        }

    });
    function cleverbot(i, user) {
        var aj = $.ajax({
            type: "POST",
            url: "/clever",
            async: true,
            data: { input: i },
            beforeSend: function() {
            },
            success: function(result) {
                lastClever = result;
                insertChat(user, result, 0);
            }
        });
        return aj.responseText;
    }

    function resetChat(){
        $("ul").empty();
    }
    function insertChat(who, text, time = 0){
        var control = "";
        var date = formatAMPM(new Date());

        if (who == "me"){
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
        setTimeout(
            function(){
        $("ul").append(control);
        var element = document.getElementById("ulid");
        element.scrollTop = element.scrollHeight;
            }, time);
    }
    //When it does the message for you
    function cprompt() {
        cleverbot(lastClever, "me");
        cleverbot(lastClever, "cleverbot");
    }
});
