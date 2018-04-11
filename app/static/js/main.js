$(document).ready(function() {
    $("#birth-date").datepicker({
        inline: true,
        showOtherMonths: true,
    });
    fillCourses();
    fillYears();
    fillDays();

    $('#birth-year, #birth-month').on('change', function() {
        fillDays();
    })

    //fill();

    $('button').on('click', function() {
        alert($("#full-name").val());
        $("#full-name").text("");
    })

    $("#student-image").on("click", function() {
        $('#select-pic').trigger('click');
    })

    window.onscroll = function() {myFunction()};
    var header = document.getElementById("header-to-stick");
    var sticky = header.offsetTop;
    function myFunction() {
        if (window.pageYOffset >= sticky) {
            header.classList.add("sticky");
        }
        else
        {
            header.classList.remove("sticky");
        }
    }

    $(".content").submit(function(event) {
    alert("ttt");
    event.preventDefault();
    if ($(".content").valid()) {
        alert('ok');
    } else {
        alert('no');
    }
    alert('done');
})

});

function fill() {
    $("#full-name").val("rr");
    $("#address").val("rr");
    $("#country").val("rr");
    $("#state").val("rr");
    $("#city").val("rr");
    $("#email").val("walidpiano@yahoo.com");
    $("#birth-date").val("10/10/2018");
    $("textarea").val("tttttt");
}

function clearAll() {
    $("#full-name").val("");
    $("#address").val("");
    $("#country").val("");
    $("#state").val("");
    $("#city").val("");
    $("#email").val("");
    $("#birth-date").val("");
    $("textarea").val("");
    $('#select-pic').val("");
    $('#student-image').attr('src', "../static/img/empty_profile.jpg");
    $("#full-name").focus();
}

function daysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#student-image')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function fillCourses() {
$.ajax({
        type: "GET",
        url: "/api/courses",
        dataType: "json",
        success: function(response) {
            $.each(response, function (index, topic) {
                $('#course').append(new Option(topic.course_name, topic.id, true, false));
            });
        }
    });
}

function fillYears() {
    var i;
    for (i=1970; i <= (new Date()).getFullYear(); i++ ) {
        $('#birth-year').append(new Option(i, i, true, false));
    };
}

function fillDays() {
    var year = $('#birth-year').val();
    var month = $('#birth-month').val();
    var numberOfDays = daysInMonth(month, year)
    $('#birth-day')
        .find('option')
        .remove()
        .end();
    var i;
    for (i=1; i <= numberOfDays; i++) {
        $('#birth-day').append(new Option (i, i, true, false));
    }

}
