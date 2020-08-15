
// 跳转到指定网页
function method_search(){
    // 发出一个地址
	var input = document.getElementById('myinput').value
    window.location.href='/app001/display?key01='+input


}

function get_input(){
	var x = document.getElementById('fname')
	document.write(x.value)
}

// function method_alert(){
//     alert("你好\n 今天天气不错")
// }
//
// function method_verify(){
// 	var x;
// 	var r=confirm("按下按钮!");
// 	if (r==true){
// 		x="你按下了\"确定\"按钮!";
// 	}
// 	else{
// 		x="你按下了\"取消\"按钮!";
// 	}
// 	document.getElementById("demo1").innerHTML=x;}
//
// function method_tips(){
// 	var x;
// 	var person=prompt("请输入你的名字","博皇");
// 	if (person!=null && person!=""){
// 	    x="你好 " + person + "今天天气怎么样?";
// 	    document.getElementById("demo2").innerHTML=x;
// 	}
// }
//
// function method_displayDate(){
// 	document.getElementById("demo3").innerHTML=Date();
// }
//
// //开始计数和停止计数
// var c=0;
// var t;
// var timer_is_on=0;
// function timedCount(){
// 	document.getElementById('txt').value=c;
// 	c=c+1;
// 	t=setTimeout("timedCount()",1000);
// }
// function doTimer(){
// 	if (!timer_is_on)
// 	{
// 		timer_is_on=1;
// 		timedCount();
// 	}
// }
// //
// function stopCount(){
// 	clearTimeout(t);
// 	timer_is_on=0;
// }
//
// // 制作时钟
// function startTime(){
// 	var today=new Date();
// 	var h=today.getHours();
// 	var m=today.getMinutes();
// 	var s=today.getSeconds();// 在小于10的数字前加一个‘0’
// 	m=checkTime(m);
// 	s=checkTime(s);
// 	document.getElementById('txt').innerHTML=h+":"+m+":"+s;
// 	t=setTimeout(function(){startTime()},500);
// }
// function checkTime(i){
// 	if (i<10){
// 		i="0" + i;
// 	}
// 	return i;
// }




