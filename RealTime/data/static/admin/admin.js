
function dateFilled(data, day, row) {
    var time = ["timestart", "timestop"];
    for (i = 0; i < 2; i++) {
        if (data[day][row][time[String(i)]] == "") {
            return false;
        }
    }
    return true;

}

function validate_input(data) {
    //for data to be moved to the student table, all input in a box 
    //i.e Course Name, Lecturer, Hall must be filled.   
    if(data!=null){var fulldata = data["timetable"];
    var days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    var placeholders = ["Course", "Lecturer", "Hall"];
    var i = 1;
    var alllFilled = false;
    for (k = 0; k < 6; k++) {
        var dayData = fulldata[String(days[k]).toLowerCase()];
        for (i = 1; i <= 4; i++) {
            var rowData = dayData[String(i)];
            var row = [];
            for (l = 0; l < 3; l++) {
                row.push(rowData[String(placeholders[l]).toLowerCase()]);
            }
            allFilled = row.includes("") ? false : true;
            for (p = 0; p < 3; p++) {
                if (row[p] != "") {
                    if (row.includes("")) {
                        alert(i);
                        return false;

                    }
                }
            }
            if (!dateFilled(fulldata, String(days[k]).toLowerCase(), i) && allFilled) {
                alert(i);
                return false;

            }
        }
    }
    return true;
}else{
    return false;
}

}

function getData() {
    var days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    var placeholders = ["Course", "Lecturer", "Hall"];
    var timestart = "timestart";
    var timestop = "timestop";
    var row_number = 4;
    var school_days_number = 6;
    var table_data = {};
    var data = {};
    for (day = 0; day < school_days_number; day++) {
        var sub_data = {};
        for (i = 0; i < row_number; i++) {
            sub_data[String(i + 1)] = {}
            sub_data[String(i + 1)][timestart] = String(document.getElementById(timestart + String(i + 1)).value);
            sub_data[String(i + 1)][timestop] = String(document.getElementById(timestop + String(i + 1)).value);
            for (placeholder = 0; placeholder < 3; placeholder++) {
                var subkey = days[day].slice(0, 3).toLowerCase() + placeholders[placeholder].toLowerCase() + String(i + 1);

                sub_data[String(i + 1)][placeholders[placeholder].toLowerCase()] = String(document.getElementById(subkey).value);
            }
        }
        table_data[days[day].toLowerCase()] = sub_data;
    }
    var specialty = String(document.getElementById('specialty').value).toLowerCase();
    var level = String(document.getElementById('level').value).toLowerCase();
    if (specialty == undefined || level == undefined) {
        alert("fill specialty,level,department");
        return null
    }
    data["specialty"] = String(document.getElementById('specialty').value).toLowerCase();
    data["level"] = String(document.getElementById('level').value).toLowerCase();
    data["timetable"] = table_data;
    return data;

}
function saveTimetable(connect) {
    var currentTimetable = getData();
    if (currentTimetable != null) {
        currentTimetable["type"] = "update.timetable";

        connect.send(JSON.stringify(currentTimetable));
    }

}

function ToStudent(connect) {
    var data = getData();
    console.log(data);
    if (validate_input(data)) {
        saveTimetable(connect);
    }

}

function createAdminTable() {
    var tableElement = document.getElementById("admin-table");
    var head = ["TIME", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    var placeholders = ["Course", "Lecturer", "Hall"];
    var rowhead = document.createElement("tr");
    var row_number = 4;
    var school_days_number = 6;
    for (indexcol = 0; indexcol < head.length; indexcol++) {
        var coltd = document.createElement("th");
        var coltddata = document.createTextNode(head[indexcol]);
        coltd.appendChild(coltddata);
        rowhead.appendChild(coltd);
    }
    tableElement.appendChild(rowhead);
    for (i = 0; i < row_number; i++) {
        var timeTableRow = document.createElement("tr");
        var time = document.createElement("td");
        var timeinput = document.createElement("input");
        var timeinput2 = document.createElement("input");
        timeinput2.type = "time";
        timeinput2.id = "timestart" + String(i + 1);
        timeinput.type = "time";
        timeinput.id = "timestop" + String(i + 1);
        // console.log(timeinput.id);
        // console.log(timeinput2.id);

        time.appendChild(document.createTextNode(" Start Time :"));
        time.appendChild(timeinput);
        time.appendChild(document.createElement("br"));
        time.appendChild(document.createTextNode(" Stop Time :"));
        time.appendChild(timeinput2);
        timeTableRow.appendChild(time);
        for (ind = 0; ind < school_days_number; ind++) {
            var colweekdata = document.createElement("td");
            var form = document.createElement("form");
            for (r = 0; r < 3; r++) {
                var inputChild = document.createElement("input");
                inputChild.type = "text";
                inputChild.id = head[ind + 1].slice(0, 3).toLowerCase() + placeholders[r].toLowerCase() + String(i + 1);
                // console.log(inputChild.id);
                inputChild.value = "";
                inputChild.placeholder = placeholders[r];
                form.appendChild(inputChild);
                form.appendChild(document.createElement("br"));
            }
            colweekdata.appendChild(form);
            timeTableRow.appendChild(colweekdata);

        }
        tableElement.appendChild(timeTableRow);

    }
}


/*
output[0].value = cell_data[0].course;
console.log(output[0].value);*/