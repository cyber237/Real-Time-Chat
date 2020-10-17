
function unpackData(data) {
    var days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    var placeholders = ["Course", "Lecturer", "Hall"];
    var starttime = "studtimestart";
    var stoptime = "studtimestop";
    if(data!="n/a"){
    var tableData = data["timetable"];
    console.log(data);


    for (day = 0; day < 6; day++) {
        for (row = 1; row < 5; row++) {
            document.getElementById(starttime + String(row)).value = tableData[days[day].toLowerCase()][String(row)]["timestart"];
            document.getElementById(stoptime + String(row)).value = tableData[days[day].toLowerCase()][String(row)]["timestop"];
            for (placeholder = 0; placeholder < 3; placeholder++) {
                var id = "stud" + days[day].slice(0, 3).toLowerCase() + placeholders[placeholder].toLowerCase() + String(row);
                var value = String(tableData[days[day].toLowerCase()][String(row)][placeholders[placeholder].toLowerCase()]);
                document.getElementById(id).value = value.length < 1 ? "_______" : value;

            }
        }
    }}


}


function createStudentTable() {
    var tableElement = document.getElementById("student-table");
    var head = ["TIME", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    var placeholders = ["Course", "Lecturer", "Hall"];
    var rowhead = document.createElement("tr");
    for (indexcol = 0; indexcol < head.length; indexcol++) {
        var coltd = document.createElement("th");
        var coltddata = document.createTextNode(head[indexcol]);
        coltd.appendChild(coltddata);
        rowhead.appendChild(coltd);
    }
    tableElement.appendChild(rowhead);
    for (i = 0; i < 4; i++) {
        var timeTableRow = document.createElement("tr");
        var time = document.createElement("td");
        var timeoutput = document.createElement("output");
        timeoutput.defaultValue = "_______";
        timeoutput.id = "studtimestart" + String(i + 1);
        var timeoutput2 = document.createElement("output");
        timeoutput2.id = "studtimestop" + String(i + 1);
        timeoutput.defaultValue = "_______";

        time.appendChild(document.createTextNode(" Start Time :"));
        time.appendChild(timeoutput);
        time.appendChild(document.createElement("br"));
        time.appendChild(document.createTextNode(" Stop Time :"));
        time.appendChild(timeoutput2);
        timeTableRow.appendChild(time);
        for (ind = 0; ind < 6; ind++) {
            var colweekdata = document.createElement("td");
            var form = document.createElement("form");
            form.className = "display cell data";
            for (r = 0; r < 3; r++) {
                var outputChild = document.createElement("output");
                outputChild.id = "stud" + head[ind + 1].slice(0, 3).toLowerCase() + placeholders[r].toLowerCase() + String(i + 1);
                outputChild.value = "_______";
                form.appendChild(outputChild);
                form.appendChild(document.createElement("br"));
            }
            colweekdata.appendChild(form);
            timeTableRow.appendChild(colweekdata);

        }
        tableElement.appendChild(timeTableRow);

    }
}