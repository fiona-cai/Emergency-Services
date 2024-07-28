let socket = io.connect("http://127.0.0.1:5000")

const onLoad = () => {
	socket.onconnect(() => {
		socket.emit("connect");
	});
};

let loadedData;

socket.on("send", (data) => {
    loadedData = data;
    console.log("data has been sent and stored")
  });

socket.on("display", () => {
    console.log("data has been confirmed and we are now displaying!")
    // set elements to data stuff 
    
})