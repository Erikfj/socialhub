$(document).ready(function(){
// Skriv all js i mellom $doc og closing brackets!

	$(".add-points-link").click(function(event) {
		event.preventDefault();
		var hub_id = $(this).data("hubid");
		var points_element_id = "#id-points-for-hub-" + hub_id;
		$.ajax({
			method: "POST",
			url: $('#add_points_url').val() + "/" + hub_id
		})
		.done(function(data){
		var points_updated = data['points_updated'];
		$(points_element_id).html(points_updated);
		});
	});


});

