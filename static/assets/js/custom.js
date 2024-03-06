var csrfmiddlewaretoken = '{{ csrf_token }}';
console.log(csrfmiddlewaretoken)

function user_edit_modal_form(id) {

    $("#exampleModalLong").modal('show');

    $.get("dashboard/account-type/" + id + "/", function(data) {
        console.log(data.name)

        document.getElementById("name").value = data.name;
        document.getElementById("edit_id").value = data.id;

        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}



function currency_edit_modal_form(id) {

    $("#exampleModal").modal('show');

    $.get("dashboard/edit_currency/" + id + "/", function(data) {
        console.log(data.name)

        document.getElementById("name").value = data.name;
        document.getElementById("edit_id").value = data.id;
        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}

function leverage_edit_modal_form(id) {

    $("#exampleModalLong").modal('show');

    $.get("dashboard/edit_leverage/" + id + "/", function(data) {
        console.log(data.name)

        document.getElementById("name").value = data.name;
        document.getElementById("edit_id").value = data.id;
        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}

function risk_delete_modal_form(id) {

    $("#exampleModalLong2").modal('show');

    $.get("dashboard/delete_risk/" + id + "/", function(data) {

        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}


function risk_delete_modal_form(id) {

    $("#exampleModalLong2").modal('show');

    $.get("dashboard/delete_risk/" + id + "/", function(data) {

        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}


// $(document).on('click', '.confirm-delete', function() {
//     $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
// });

// $(document).on('click', '#confirmDeleteButtonModal', function() {
//     var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
//     window.location = $("#".concat(caller)).attr("href");
// });


function currencygroup_edit_modal_form(id) {
    console.log(window.location.href)
    var h = location.pathname;
    console.log(h)
    $("#exampleModalLong1").modal('show');

    $.get("groups/edit_currency_group/" + id + "/", function(data) {
        console.log(data.name)

        document.getElementById("name").value = data.name;
        document.getElementById("edit_id").value = data.id;
        if (data == 1) {
            location.reload();
        } else {
            $("#example1").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}

function currencysymbol_edit_modal_form(id) {
    console.log(window.location.href)
    var h = location.pathname;
    console.log(h)
    $("#exampleModal_new").modal('show');

    $.get("groups/edit_currency_symbol/" + id + "/", function(data) {
        console.log(data)

        document.getElementById("group").value = data.group;
        document.getElementById("edit_id").value = data.id;
        document.getElementById("symbol").value = data.symbol;
        if (data == 1) {
            location.reload();
        } else {
            $("#example1").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}

// $("#mobile").on("focusout", function() {

//     Phone_number = $(this).val();
//     console.log(Phone_number)
//     var phoneno = /^\d{10}$/;
//     if (Phone_number.match(phoneno)) {
//         console.log('hhh')
//     } else {
//         alert("Not a valid Phone Number");
//         // $("#passwd1_error").text("Not a valid Phone Number");

//     }


// });

function mt5_group_edit_modal_form(id) {

    $("#exampleModal").modal('show');

    $.get("dashboard/edit_currency/" + id + "/", function(data) {
        console.log(data.name)

        document.getElementById("name").value = data.name;
        document.getElementById("edit_id").value = data.id;
        if (data == 1) {
            location.reload();
        } else {
            $("#data_process_modal").modal('hide');
            if (data == 0) {
                alert("Invalid operation");
            }
            if (data == 2) {
                alert("User not Found, Contact Administrator");
            }
        }
    });

}

// $(document).on('click', '#sendMessageButton', function(e) {
//     swal(
//         'Success',
//         'You clicked the <b style="color:green;">Success</b> button!',
//         'success'
//     )
// });



function confirmDelete() {
    swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            closeOnConfirm: false
        },
        function(isConfirm) {
            console.log('jjjjj')
            if (isConfirm) {
                $.ajax({
                    url: "live_deposit_api_call",
                    type: "POST",
                    // data: { id: 5 },
                    dataType: "html",
                    success: function() {
                        swal("Done!", "It was succesfully deleted!", "success");
                    }
                });
            } else {
                swal("Cancelled", "Your imaginary file is safe :)", "error");
            }
        })
}