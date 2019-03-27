//DataTables
$(function () {
	var table = $('.tabla-generica').DataTable({
		responsive: true,
	    language: {
	        "decimal": "",
	        "emptyTable": "No hay información",
	        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
	        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
	        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
	        "infoPostFix": "",
	        "thousands": ",",
	        "lengthMenu": "Mostrar _MENU_ Entradas",
	        "loadingRecords": "Cargando...",
	        "processing": "Procesando...",
	        "search": "Buscar:",
	        "zeroRecords": "Sin resultados encontrados",
	        "paginate": {
	            "first": "Primero",
	            "last": "Ultimo",
	            "next": "Siguiente",
	            "previous": "Anterior"
	        }
	    },
	});
});


jQuery(document).ready(function(){
	var location = window.location.pathname;
	if (location=="/citas/agregar/" || location.includes("/citas/editar/")) {
		//Date picker
	    $('#datepicker').datepicker({
	    	autoclose: true,
	    	startDate: "yesterday",
	    })
	    //Timepicker
	    $('.timepicker').timepicker({
	      showInputs: false,
	      showMeridian: false,
	      minuteStep: 1,
	    })
	}
});