const fila = document.querySelector('.contenedor-carousel');
const platos = document.querySelectorAll('.plato');

const flechaIzquierda = document.getElementById('flecha-izquierda');
const flechaDerecha = document.getElementById('flecha-derecha');



var btnAbrirPopupRep = document.getElementById("btn-abrir-Reprod"),
	overlayRep = document.getElementById("overlayReproduction"),
	popupRep = document.getElementById("popupRep"),
	btnCerrarPopupRep = document.getElementById("btn-cerrar-popupRep");

btnAbrirPopupRep.addEventListener("click", function () {
	overlayRep.classList.add("active")
	popupRep.classlist.add("active")
	
});
btnCerrarPopupRep.addEventListener("click", function () {
	overlayRep.classList.remove("active") 
	popupRep.classlist.remove("active")
});



var btnAbrirPopupinfor = document.getElementById("btn-abrir-infor"),
	overlayinfor = document.getElementById("overlayinformacion"),
	popupinfor = document.getElementById("popupinfor"),
	btnCerrarPopupinfor = document.getElementById("btn-cerrar-popupinfor");

btnAbrirPopupinfor.addEventListener("click", function () {
	overlayinfor.classList.add("active")
	popupinfor.classlist.add("active")

});
btnCerrarPopupinfor.addEventListener("click", function () {
	overlayinfor.classList.remove("active") 
	popupinfor.classlist.remove("active")
});


// ? ----- ----- Event Listener para la flecha derecha. ----- -----//
flechaDerecha.addEventListener('click', () => {
	fila.scrollLeft += fila.offsetWidth;

	const indicadorActivo = document.querySelector('.indicadores .activo');
	if(indicadorActivo.nextSibling){
		indicadorActivo.nextSibling.classList.add('activo');
		indicadorActivo.classList.remove('activo');
	}
});

// ? ----- ----- Event Listener para la flecha izquierda. ----- -----
flechaIzquierda.addEventListener('click', () => {
	fila.scrollLeft -= fila.offsetWidth;

	const indicadorActivo = document.querySelector('.indicadores .activo');
	if(indicadorActivo.previousSibling){
		indicadorActivo.previousSibling.classList.add('activo');
		indicadorActivo.classList.remove('activo');
	}
});

// ? ----- ----- Paginacion ----- -----
const numeroPaginas = Math.ceil(platos.length / 5);
for(let i = 0; i < numeroPaginas; i++){
	const indicador = document.createElement('button');

	if(i === 0){
		indicador.classList.add('activo');
	}

	document.querySelector('.indicadores').appendChild(indicador);
	indicador.addEventListener('click', (e) => {
		fila.scrollLeft = i * fila.offsetWidth;

		document.querySelector('.indicadores .activo').classList.remove('activo');
		e.target.classList.add('activo');
	});
}

// ? ----- ----- Hover ----- -----
platos.forEach((plato) => {
	plato.addEventListener('mouseenter', (e) => {
		const elemento = e.currentTarget;
		setTimeout(() => {
			platos.forEach(plato => plato.classList.remove('hover'));
			elemento.classList.add('hover');
		}, 300);
	});
});

fila.addEventListener('mouseleave', () => {
	peliculas.forEach(plato => plato.classList.remove('hover'));
});

