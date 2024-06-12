<template>

   <NavBar/>               <!--All the HTML and CSS components are imported in the main page to display the navigation bar-->

   <!--This is the HTML tags to develop the form for adding the task details-->
   <!--The v-model syntax is used to store the user input into the variables that are stated in the double quotes-->
   <!--The required keyword is used to ensure that the user types something on the text field and uploads an image-->
   <!--After the user has filled in the form, and clicked the submit button, the inserttask() function will be called and execute its code-->

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

     <br>

     <h2 class="h1">
         <b>Add a Task</b>
     </h2>

     <br>

     <div class="form-group">
       <form method="POST" enctype="multiple/form-data" v-on:submit.prevent="inserttask();">
         <div class="mb-3">
         <legend for="name1">Enter the name of the task</legend><br>
         <input class="form-control" type="text" v-model="name1" id="name1" name="name1" placeholder="Enter the name of the task" required><br><br>
         </div>
         <div class="mb-3">
         <legend for="date">Enter the date to start the task</legend><br>
         <input class="form-control" type="date" v-model="date" id="date1" name="date" required><br><br>
         </div>
         <div class="mb-3">
         <legend for="time">Enter the time to start the task</legend><br>
         <input class="form-control" type="time" v-model="startTime" id="startTime1" name="startTime" required><br><br>
         </div>
         <div class="mb-3">
         <legend for="amountOfTime">Enter the amount of time to spend the task</legend><br>
         <input class="form-control" type="time" v-model="amountOfTime" id="amountOfTime1" name="amountOfTime" placeholder="Enter the task description" required><br><br>
         </div>
         <div class="mb-3">
         <legend for="descriptionOfTheTask">Write the description of the task</legend><br>
         <input class="form-control" type="text" v-model="descriptionOfTheTask" id="descriptionOfTheTask1" name="descriptionOfTheTask" required><br><br>
         </div>
         <div class="mb-3">
         <legend for="uploadingTheImage">Upload the image</legend><br>
         <input class="form-control" type="file" id="image" placeholder="Upload the picture" required/><br><br>
         </div>
         <button type="submit" class="btn btn-sm btn-primary mt-3 custom-btn">Submit</button><br><br>
       </form>
     </div>
   </div>
   <div>
   </div>

   <br>

   <!--This is where it displays the list of task details and the two buttons, which are the update button and the delete button-->

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
   <div class="h1">
         Retrieve the task detail
   </div>
   <br>
   <div v-if="taskdetail.length>0">                 <!--First it checks if there are any task details stored in the database-->
      <div class="row-container">                     <!--predefined bootstrap class will display the task details row by row-->
       <div v-for="task_details in taskdetail" class="row-item">               <!--The v-for syntax iterates the task details which are stored in the taskdetail variable-->
          <div v-if="task_details.id !=null">

             <!--The task details will be displayed using the html tags with predefined bootstrap class, which are card-body, card-title, card-text, and card-img-top.-->
             <!--All the details will be accessed by the field by using the dot notation-->

             <div class="card" style="width: 18rem;">

                <img :src="task_details.image" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">Task Name: {{task_details.name}}</h5>
                <p class="card-text">Task Start Date: {{task_details.date}}</p>
                <p class="card-text">Task Start Time: {{task_details.startTime}}</p>
                <p class="card-text">Amount of time to spend on the task: {{(task_details.amountOfTime).split(":")[0]}} hours and {{(task_details.amountOfTime).split(":")[1]}} minutes</p>
                <p class="card-text">Description of the task: {{task_details.descriptionOfTheTask}}</p>
                <button @click="deleteTask(task_details.id)" class="btn btn-danger ml-2">Delete</button><span style="padding-right: 20px"></span>     <!--This is where delete button will be displayed. Once the user clicks it, the deletetask() function will be called with the task's id passed to the parameter. It's code will be executed to delete the task with a particular task id.-->
                <button @click="navigateToUpdate(task_details.id)" class="btn btn-primary">Update</button>          <!--This is where the update button will be displayed. Once the user clicks it, the navigateToUpdate() function will be called with the task's id passed to the parameter. It's code will be executed to redirect the user to another URL that provides the form to update the task details of a particular task id.-->
                </div>
             </div>
          </div>
         </div>
     </div>
     </div>
     </div>

   <br>

   <!--This is the button to click to execute the automated testing-->

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

     <form method="POST" enctype="multiple/form-data" v-on:submit.prevent="tests();">

         <button class="btn btn-primary" type="submit">Test the web app</button>

     </form>

   </div>

</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import UpdateTask from '../components/UpdateTask.vue';
import DeleteTask from '../components/DeleteTask.vue';
import RetrieveTask from '../components/RetrieveTask.vue';
import NavBar from '../components/NavBar.vue';
export default{
       //This is the starting point to import the code from the NavBar.vue file
       components:{
           NavBar,
       },
       //The variables below are variables to store the user inputs from the form fields
       data(){
           return{
              name1:"",
              date:"",
              startTime:"",
              amountOfTime:"",
              descriptionOfTheTask:"",
              image:null,
              queryForVideos:"",
              listOfFoodItems:"",
              query:"",
              amountOfCalories:"",
              dietType:"",
              mealType:"",
              taskdetail:[],
           }
       },
       methods:{

        //The tests function executes the print_test_results python function, which mapped to the /test_results/.
        //It's defined in the urls.py file in the protocolApplication folder

        async tests(){


           //The specified Django URL endpoint is fetched using the GET http method.
           //The credentials have a field that stores a include value, which will remember which user is logged in.

           let response = await fetch("http://localhost:8000/test_results/",{

                    method: 'GET',
                    credentials: "include"

           })

           var testResults = await response.json()

           console.log(testResults.test_results[0])

        },

        async resizeInput(){

              this.style.width = this.value.length +"ch";

        },



        //This javascript function fetched all the task details from the database that belongs to the logged in user

        async fetchtaskdetails(){



        //The div elements is created to store the retrieved html elements from the DOM tree.

        let taskDiv = document.createElement('div');
        taskDiv.className = 'col-12 col-sm-6 col-md-4';
        taskDiv.id = "taskholder"



        //The response variable stores the tasks from the database, which is returned from the python function that is mapped from the /RetrieveTaskDetails/ URL path.
        //The python function in the views.py file is called RetrieveTask. The HTTP GET method is used to retrieve the data from the python function
        //and that data is the task detail.

        let response = await fetch("http://localhost:8000/RetrieveTaskDetails/", {
              method: 'GET',
              credentials: "include"
        })
        let data = await response.json()        //The tasks details is converted to the JSON format.
        this.taskdetail = data.task;            //The task field is accessed where all the user's task details are there and it gets stored to the taskdetail variable.




        //The task details are iterated by the forEach built-in function. The fields of the fetched task details are accessed by the dot notation and are displayed by the HTML elements.
        //The predefined bootstrap classes are used as before and it displays the task details in a card shaped boxes. The boxes have the size of 100px by 100px.
        //All of the HTML elements are stored in the div tag that has got the id of taskholder.

        data.task.forEach(task => {

            taskDiv.innerHTML += `
                <div id="${task.id}" class="card w-100 h-100">
                    <img class="card-img-top" style="height: 300px; object-fit: cover" src="${task.image}" alt="Task">
                        <div>
                            <h5 class="card-title">Task Name: ${task.name}</h5>
                            <p class="card-text">Starting date by ${task.date}</p>
                            <p class="card-text">Starting time by ${task.startTime}</p>
                            <p class="card-text">Amount of time by ${task.amountOfTime}</p>
                            <p class="card-text">The Description of the task: ${task.descriptionOfTheTask}</p><br>
                        </div>
                </div>
            `;

        })

       taskDiv.style.visibility = "hidden";

       taskDiv.style.display = "None";

       //The if statement will prevent the fetching the same HTML elements every time the user clicks the fetch button, by checking if the div tag with the id called taskholder
       //already exists or not. If it does exists, then it will be removed from the DOM tree root.

       if(document.body.contains(document.getElementById("taskholder"))){

          document.body.removeChild(document.getElementById("taskholder"));

       }



       //It will be appended to the DOM tree root.

       document.body.appendChild(taskDiv);




       //The starting time to retrieve the HTML elements from the DOM tree is recorded
       const start = performance.now();




       //This where the document is printed on the screen to see the fetched HTML elements.

       console.log(document.getElementById("taskholder"));


       //This finishing time to fetch the HTML elements from the DOM tree root is recorded
       const end = performance.now();




       //The time taken to fetch HTML elements is calculated
       console.log(`DOM fetching time took ${end - start} milliseconds.`);

       },

       async deleteTask(taskId){
              let response = await fetch("http://localhost:8000/DeleteTaskDetail/", {
                method:'POST',
                credentials: "include",
                headers: {
                     'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                      deleteid: taskId
                })
              });
              console.log("emit event...")
              //this.$emit("task-detail-deleted");

              console.log(response.status)

              /*
              if(response.status!=200){
                 //errorMessageForDelete = 'Invalid task ID. Please enter a valid ID.';
                 document.getElementById("errorMessageForDelete").innerHTML = 'Invalid task ID. Please enter a valid ID.';
                 return;
              }

              else{

                this.taskdetail = this.taskdetail.filter(task => task.id !== taskId);

                document.getElementById("errorMessageForDelete").innerHTML = '';

              }
              */

              this.taskdetail = this.taskdetail.filter(task => task.id !== taskId);

              let data= await response.json()

              const start = performance.now();

              document.getElementById(data.task_detail[0].id).innerHTML = ``;

              const end = performance.now();

              console.log(`DOM fetching time took ${end - start} milliseconds.`);

       },

       navigateToUpdate(taskId) {
             this.$router.push({ name: 'UpdateTask', params: { id: taskId } });
       },

        //The javascript function called inserttask() is used to capture the user input from the form and pass it to the python function which is mapped to the /TaskInsert/ path URL.
        //That python function is called AddTask in the view.py file. The POST http method is used to add data to the database and the data is task details.
        //The credentials field is used to remember the user who is currently logged in by storing the include value.
        //This function will also measure the time taken to insert HTML elements to the DOM tree.

        async inserttask(){

         var fd = new FormData();
         fd.append('name1', this.name1)
         fd.append('date', this.date)
         fd.append('startTime', this.startTime)
         fd.append('amountOfTime', this.amountOfTime)
         fd.append('descriptionOfTheTask', this.descriptionOfTheTask)
         fd.append('image', document.getElementById('image').files[0])
         let response = await fetch("http://localhost:8000/TaskInsert/",{
            method: 'POST',
            credentials: "include",
            body: fd
         })


       //The result returned in the response variable from the AddTask python function, it's converted to a JSON format.

       var data= await response.json()

       console.log(data.task_detail[0].id)



       //The div element is created with the id called taskholder. The if statement checks if that div element already exists or not.
       //If yes then a message is printed on the console saying that that div tag element exists. If not then, it sets the div element class to 'col-13 col-sm-6 col-md-4'.
       //It also sets the id to taskholder. It's HTML content will be set to an empty string. After that, the the div HTMl element will be added to root of the DOM tree.
       //This prevents the div tag to be added multiple times to the DOM tree, if the submit button is clicked multiple times in the add form.

       let element = document.getElementById('taskholder');

       console.log(element);

       if(element){
           console.log('Element with id "taskholder" exists.');
       }

       else{

           let taskDiv = document.createElement('div');
           taskDiv.className = 'col-12 col-sm-6 col-md-4';
           taskDiv.id = "taskholder"
           //taskDiv.innerHTML = ``;
           taskDiv.innerHTML = ``;

           document.body.appendChild(taskDiv);

       }



       //The start time to add the HTMl elements to the DOM is recorded

       const start = performance.now();



       //As soon as the user input is captured and stored in the data variable, all of it's feilds will be interated using the forEach function and display them in a white box, which looks like cards using the HTML elements.
       //The white box will have a size of 100px by 100px. The predefined bootstrap class will be imported, which are card-img-top, card-title, and card-text to display the task details into card shaped boxes.

       data.task_detail.forEach(task => {

        document.getElementById("taskholder").innerHTML +=`
             <div id="${task.id}" style="display: none; height: 100px;" class="card w-100 h-100">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${task.image}" alt="Task">
              <div>
               <h5 class="card-title">${task.name}</h5>
               <p class="card-text">Starting date by ${task.date}</p>
               <p class="card-text">Starting time by ${task.startTime}</p>
               <p class="card-text">Amount of time by ${task.amountOfTime}</p>
               <p class="card-text">The Description of the task ${task.descriptionOfTheTask}</p>
              </div>
             </div>
            </div>
        `;

       })



       //The finishing time of inserting the HTML elements into the DOM tree will be recorded.

       const end = performance.now();



       //The time taken to insert the HTML elements into the DOM is calculated.

       console.log(`DOM insertion time took ${end - start} milliseconds.`);

       console.log(document)

       this.fetchtaskdetails();

       },

   },

    //The mounted function is where the vue framework automatically calls the function called fetchtaskdetails to fetch the task details that are stored in the database straight away.
    mounted(){

        this.fetchtaskdetails();

    }

}
</script>

//This css style where it executes the colour change in the background form and makes the colour of the form buttons blue.
//When you hover the form buttons, the button colour changes from the regular blue to dark blue.

<style scoped>

@keyframes gradientAnimation {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.animated-background {
    background: linear-gradient(270deg, #ff7e5f, #feb47b);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
}

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0.5, 0.5, 0.5, 0.5);
}

.custom-btn {
  background-color: #007bff; /* Primary color */
  border-color: #007bff;
  font-weight: bold;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.custom-btn:hover {
  background-color: #0056b3; /* Darker shade for hover effect */
  border-color: #004085;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.custom-btn:focus {
  outline: none;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}

.custom-btn:active {
  background-color: #004085;
  border-color: #003366;
}

header {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}

</style>