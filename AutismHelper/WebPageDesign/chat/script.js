// 成功发送
var send_message=document.getElementById("chat_middle_item");
var domBtm=document.getElementById("button");
// 发送内容
var message=document.getElementById("chat_context_item");
domBtm.addEventListener("click",function(){
    var str=message.value;
    var date=new Date();
    var hour=date.getHours();
    var mm=date.getMinutes();
    var time=hour+':'+mm;
    var ans='<div class="chat_right_item_1 clearfix">您</div>'+
        '<div class="chat_right_item_2">'+
            '<div class="chat_right_time clearfix">'+time+'</div>'+
            '<div class="chat_right_content clearfix">'+str+'</div>'
            +'</div>';
    var oLi=document.createElement("div");
    oLi.setAttribute("class","chat_right");
    oLi.innerHTML=ans;
    send_message.append(oLi);
    message.value="";
});