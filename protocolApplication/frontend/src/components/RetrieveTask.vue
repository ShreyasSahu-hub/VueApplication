<template class="p-3 mb-2 bg-light text-dark">

   <!-- This is the HTML element to develop the Task List form -->


   <!--Remember any form that is inside this type of div tag will have an animation background because this div tag makes it happen.-->
   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">


   <!--This button will be clicked by the user and it will call the fetchtasdetails() function which is implemented further down this file to fetch all the task details that belongs to the user-->

   <br><button @click="fetchtaskdetails();" class="btn btn-sm btn-primary mt-3 custom-btn">Fetch all the task details at all the dates</button><br><br>



     <!--This is where it displays the list of task details and the two buttons, which are the update button and the delete button-->

     <div class="h1">
         Retrieve the task detail
     </div>
     <br>
     <div v-if="taskdetail.length>0">                 <!--First it checks if there are any task details stored in the database-->
      <div class="row-container">                     <!--predefined bootstrap class will display the task details row by row-->
       <div v-for="task_details in taskdetail" class="row-item">               <!--The v-for syntax iterates the task details which are stored in the taskdetail variable-->
          <div v-if="task_details.id !=null">
             <!--<tr bgcolor="#D6EEEE">
             <th>Task id</th>
             <th>Task Name</th>
             <th>Task Start Date</th>
             <th>Task Start Time</th>
             <th>Amount of time to spend on the task</th>
             <th>Description of the task</th>
             <th>Task image</th>
             <th>Want to delete this task?</th>
             <th>Want to update the details of this task</th>
             </tr>
             <tr>
             <td>{{task_details.id}}</td>
             <td>{{task_details.name}}</td>
             <td>{{task_details.date}}</td>
             <td>{{task_details.startTime}}</td>
             <td>{{task_details.amountOfTime}}</td>
             <td>{{task_details.descriptionOfTheTask}}</td>
             <td><img :src="task_details.image" height="200" width="200"/></td>
             <td><button @click="deleteTask(task_details.id)" class="text-danger" style="color: red;">Delete</button></td>
             #<td><a href="/updateTask"><button style="color: blue;">Update</button></a></td>
             <td><button @click="navigateToUpdate(task_details.id)" style="color: blue;">Update</button></td>
             </tr>-->



             <!--The task details will be displayed using the html tags with predefined bootstrap class, which are card-body, card-title, card-text, and card-img-top.-->
             <!--All the details will be accessed by the field by using the dot notation-->

             <div class="card" style="width: 18rem;">

                <img :src="task_details.image" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">Task Name: {{task_details.name}}</h5>
                <p class="card-text">Task Start Date: {{task_details.date}}</p>
                <p class="card-text">Task Start Time: {{task_details.startTime}}</p>
                <p class="card-text">Amount of time to spend on the task: {{task_details.amountOfTime}}</p>
                <p class="card-text">Description of the task: {{task_details.descriptionOfTheTask}}</p>
                <button @click="deleteTask(task_details.id)" class="text-danger" style="color: red;">Delete</button>      <!--This is where delete button will be displayed. Once the user clicks it, the deletetask() function will be called with the task's id passed to the parameter. It's code will be executed to delete the task with a particular task id.-->
                <button @click="navigateToUpdate(task_details.id)" style="color: blue;">Update</button>          <!--This is where the update button will be displayed. Once the user clicks it, the navigateToUpdate() function will be called with the task's id passed to the parameter. It's code will be executed to redirect the user to another URL that provides the form to update the task details of a particular task id.-->
                </div>
             </div>
          </div>
         </div>
     </div>
     </div>
   </div>
</template>

<script>

import { ref, onMounted } from 'vue';

export default{

   //The taskdetail variable is created to store the task details that are posted by the user
   //The id variable is created to store the task id.

   data(){

      return{
       taskdetail:[],
       id:"",
      }

   },
   methods:{

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

    },

    mounted(){

       this.fetchtaskdetails();

    }

}
</script>

<style>
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

.row-container {
  display: flex;
  flex-wrap: wrap; /* Allow items to wrap to the next line */
  justify-content: space-around; /* Adjust as needed */
}

</style>