//=socket
socket = io();

socket.on('message', function(msg){
	insert(msg);
});

send.onsubmit=()=>{
	let msg = typer.value.trim();
	socket.send(msg);
	insert(msg);
	typer.value='';
	return false;
}

function insert(msg){
	msgbox.insertAdjacentHTML('afterBegin', `<div>${msg}</div><br>`);
}

