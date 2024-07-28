let socket = io.connect("http://127.0.0.1:5000")

const onLoad = () => {
	socket.onconnect(() => {
		socket.emit("connect");
	});
};

socket.on("send", (data) => {
    console.log("data has been sent and stored")
    // now put text from data into the elements
    
});