let cuadrado

function setup() {
	createCanvas(400, 400);
}

function draw() {
	//dibujo de un cuadrado utilizando p5. Los bordes son negros para aplicar el algoritmo FloodFill en el coloreo
	//los primeros parametros son la pos y el ultimo es el tamaño
	cuadrado = square(0,0,100)
	//getPixelArray(cuadrado)
	console.log(cuadrado.get(50 , 50))
	let bg = cuadrado.get(50 , 50)
	FloodFill(5, 25, bg)

	//agregar un floodfill aqu?
	
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

function FloodFill(x, y, bg){
	//coordenadas
	let pix = get(x, y)
	console.log(pix)
	if (verificarColor(bg, pix)){
		console.log('Iniciando floodfill en el ' + x + ', ' + y)
		set(x, y, color(0))
		FloodFill(x + 1, y, bg)
		FloodFill(x - 1, y, bg)
		FloodFill(x, y + 1, bg)
		FloodFill(x, y - 1, bg)

	}
	updatePixels()

}

function verificarColor(arr1, arr2){
	return arr1[0]==arr2[0] && arr1[1]==arr2[1] && arr1[2]==arr2[2] && arr1[3]==arr2[3]
}