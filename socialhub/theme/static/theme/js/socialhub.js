$(document).ready(function(){
// Skriv all js i mellom $doc og closing brackets!

	$(".add-points-link").click(function(event) {
		event.preventDefault();
		var note_id = $(this).data("noteid");
		var points_element_id = "#id-points-for-note-" + note_id;
		$.ajax({
			method: "POST",
			url: $('#add_points_url').val() + "/" + note_id
		})
		.done(function(data){
		var points_updated = data['points_updated'];
		$(points_element_id).html(points_updated);
		});
	});


});

