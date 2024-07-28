const URL = 'https://fcaiona.pythonanywhere.com'; //'http://localhost:5000'; // set to undefined for production
let socket = io.connect(URL)

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
    document.getElementById('instr1').innerText = loadedData.firefighters_equipment;
    document.getElementById('instr2').innerText = loadedData.firefighters_safety;
    document.getElementById('instr3').innerText = loadedData.firefighters_instructions;
    document.getElementById('instructions').innerText = "Instructions for " + loadedData.firefighters + " units";
})