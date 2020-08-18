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