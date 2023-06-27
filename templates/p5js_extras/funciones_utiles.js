function grabar(){
if (frameCount === 1) {
const capture = P5Capture.getInstance();
capture.start({
format: "mp4",
duration: 100,
	});
  }
}

function createColor(){
	colorMode(HSB)
	let h = random(255)
	let s = random(255)
	let b = random(255)
	return color(h, s, b)
}