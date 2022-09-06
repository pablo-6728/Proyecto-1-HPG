let cuadrado

function setup() {
	createCanvas(400, 400);
}

function draw() {
	//dibujo de un cuadrado utilizando p5. Los bordes son negros para aplicar el algoritmo FloodFill en el coloreo
	//los primeros parametros son la pos y el ultimo es el tamaño
	cuadrado = square(100,100,200)
	getPixelArray(cuadrado)
	//FloodFill(50, 25, cuadrado)
	noLoop()
}

//TODO: hacer la funcion de relleno de color
function getPixelArray(shape){
	//variables de posicion
	let x, y, pix
	//let pix = shape.get(0, 0)
	let color = []
	

	//asignar los valores al array de color
	for (x = 0; x < 100; x++){
		for (y = 0; y < 100; y++){
			pix = shape.get(x, y)
			color[x] = pix
		}
	}
	//console.log(color[1])
	//console.log(color)
	FloodFill(50, 25, color[0])

}

function FloodFill(x, y, coloraArray){
	let c = color(255, 204, 0) 
	console.log('Iniciando floodfill')
	console.log('Floodfill en ' + x + ', ' + y)
	if(coloraArray[0] == [0, 0, 0, 0]){
		set(x, y, c)
		FloodFill(x+1, y, coloraArray[x + 1])
		FloodFill(x-1, y, coloraArray[x + 1])
		FloodFill(x, y+1, coloraArray[x + 1])
		FloodFill(x, y-1, coloraArray[x + 1])

		updatePixels()
	}
	
}