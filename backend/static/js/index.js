const URL = process.env.NODE_ENV === 'production' ? undefined : 'http://localhost:5000';
let socket = io.connect(URL)

const onLoad = () => {
	socket.onconnect(() => {
		socket.emit("connect");
	});
};

socket.on("send", (data) => {
    console.log("data has been sent and stored")
    // now put text from data into the elements
    
});