<template>

   <NavBar/>

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

     <br>
     <h2 class="my-4">
         Update a Task
     </h2>
     <br>

     <form method="POST" v-on:submit.prevent="updatetask();">
          <div class="mb-3">
          <legend for="name">Enter the name of the task</legend><br>
          <input class="form-control" type="text" v-model="name" id="name1" name="name" placeholder="Enter the name of the task" required><br><br>
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
          <input class="form-control" type="file" id="image" placeholder="Upload the picture" required/><br>
          </div>
          <button type="submit" class="btn btn-sm btn-primary mt-3 custom-btn">Submit</button><br><br>
     </form>

   </div>
</template>

<script>
import NavBar from '../components/NavBar.vue';
export default{
       components:{
         NavBar,
       },
       data(){
           return{
              name:"",
              date:"",
              startTime:"",
              amountOfTime:"",
              descriptionOfTheTask:"",
              image:"",
              id:"",
              errorMessage:"",
           }
       },
       methods:{

        async resizeInput(){

              this.style.width = this.value.length +"ch";

        },

        async updatetask(){

         var fd = new FormData();
         var file = document.getElementById('image').files[0]
         console.log(file);
         fd.append('update_id', this.$route.params.id)
         fd.append('update_name', this.name)
         fd.append('update_date', this.date)
         fd.append('update_startTime', this.startTime)
         fd.append('update_amountOfTime', this.amountOfTime)
         fd.append('update_descriptionOfTheTask', this.descriptionOfTheTask)
         fd.append('update_image', document.getElementById('image').files[0])
         let response = await fetch("http://localhost:8000/TaskUpdate/",{
            method: 'POST',
            credentials: "include",
            body: fd
         })

         /*
         if(response.status!=200){
            //errorMessage = 'Invalid task ID. Please enter a valid ID.';
            document.getElementById("errorMessage").innerHTML = `Invalid task ID. Please enter a valid ID.`
            return;
         }
         */

         let data = await response.json()

         //console.log(data.update_taskdetail.id)

         const start = performance.now();

         document.getElementById(data.update_taskdetail[0].id).innerHTML = `
            <div class="card-body d-flex flex-column justify-content-between gap-4">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${data.update_taskdetail[0].image}" alt="Task">
              <div>
               <h5 class="card-title">${data.update_taskdetail[0].name}</h5>
               <p class="card-text">Starting date by ${data.update_taskdetail[0].date}</p>
               <p class="card-text">Starting time by ${data.update_taskdetail[0].startTime}</p>
               <p class="card-text">Amount of time by ${data.update_taskdetail[0].amountOfTime}</p>
               <p class="card-text">The Description of the task ${data.update_taskdetail[0].descriptionOfTheTask}</p>
              </div>
            </div>
         `;

         const end = performance.now();

         console.log(`DOM updating time took ${end - start} milliseconds.`);

         console.log(document)

         this.$router.replace('/mainPage');

       },

      }

}
</script>

<style scoped>
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

.animated-background {
    background: linear-gradient(270deg, #ff7e5f, #feb47b);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
}

</style>