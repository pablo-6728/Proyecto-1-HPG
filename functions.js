let cuadrado
let cuadradoLen = 90

function setup() {
	createCanvas(400, 400);
}

function draw() {
	//dibujo de un cuadrado utilizando p5. Los bordes son negros para aplicar el algoritmo FloodFill en el coloreo
	//los primeros parametros son la pos y el ultimo es el tamaño
	cuadrado = square(0, 0, cuadradoLen)
	console.log(cuadrado.get(50 , 50))
	let bg = cuadrado.get(cuadradoLen/2 , cuadradoLen/2)
	FloodFill(5, 10, bg)	
	noLoop()
}

//funcion FloodFill para colorear
function FloodFill(x, y, bg){
	//coordenadas
	let pix = get(x, y)
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

//funcion que verifica que el array 1 sea igual al 2 en RGB
function verificarColor(arr1, arr2){
	return arr1[0]==arr2[0] && arr1[1]==arr2[1] && arr1[2]==arr2[2] && arr1[3]==arr2[3]
}