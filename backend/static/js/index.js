const URL = 'http://localhost:5000'; //'http://localhost:5000'; // set to undefined for production
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