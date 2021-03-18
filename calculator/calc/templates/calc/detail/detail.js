$(document).on('click', '#submit-btn', function(event){
    var storage_data = {}
    var trucks_data = $('.Trucks');
    for(i=0;i<trucks_data.length;i++){
        var storage_id = $(trucks_data[i]).find('.storage_id').text();
        var truck_id = $(trucks_data[i]).find('.truck_id').text();
        var coordinate_x = $(trucks_data[i]).find('#point_x_input').val();
        var coordinate_y = $(trucks_data[i]).find('#point_y_input').val();
        if (storage_data[storage_id]) {
            storage_data[storage_id]["trucks_data"][truck_id] = {
                "coordinate_x" : coordinate_x,
                "coordinate_y" : coordinate_y,
            };
        } else {
            storage_data[storage_id] = {
                'trucks_data': {}
                };
            storage_data[storage_id]["trucks_data"][truck_id] = {
                "coordinate_x" : coordinate_x,
                "coordinate_y" : coordinate_y,
            };
        }
    }
    response_data = {
        "storage_data":storage_data
    }
    $.ajax({
            type: "POST",
            url: "coordinate_update/",
            data: {data: JSON.stringify(response_data),
                csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function(response){
                alert("Расчеты произведены, нажмите OK для загрузки");
                window.location.reload() 
            }
        });
});