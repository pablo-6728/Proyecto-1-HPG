let cuadrado

function setup() {
	createCanvas(400, 400);
}

function draw() {
	//dibujo de un cuadrado utilizando p5. Los bordes son negros para aplicar el algoritmo FloodFill en el coloreo
	//los primeros parametros son la pos y el ultimo es el tamaño
	cuadrado = square(0,0,200)
	//getPixelArray(cuadrado)
	console.log(cuadrado.get(50 , 50))
	FloodFill(50, 50)
	noLoop()
}

//TODO: hacer la funcion de relleno de color
function getPixelArray(shape){
	//variables de posicion
	let x, y, pix
	//let pix = shape.get(0, 0)
	let colorx = []
	let colory = []
	

	//asignar los valores al array de color
	for (x = 0; x < 100; x++){
		for (y = 0; y < 100; y++){
			pix = shape.get(x, y)
			colory[y] = pix
		}
		pix = shape.get(x, y)
		colorx[x] = pix
	}
	//console.log(color[1])
	//console.log(color)
	//FloodFill(50, 25, color[0])
	console.log(colorx)
	console.log(colory)
}

function FloodFill(x, y){
	//coordenadas
	
	let pix = get(x, y)
	console.log(pix)
	if (pix === [255, 255, 255, 255]){
		console.log('Iniciando floodfill en el ' + x + ', ' + y)
		set(x, y, 0)
		FloodFill(x + 1, y)
		FloodFill(x - 1, y)
		FloodFill(x, y + 1)
		FloodFill(x, y - 1)

	}
	updatePixels()

}