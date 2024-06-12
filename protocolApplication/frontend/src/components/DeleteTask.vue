<template class="p-3 mb-2 bg-light text-dark">
   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

     <br>
     <h2 class="my-4">
         Delete the task detail in this form
     </h2>

     <form method="POST" v-on:submit.prevent="deleteTask();">
         <legend for="id">Enter the id of the task</legend><br>
         <input class="form-control" type="text" v-model="id" id="id" name="id" onkeypress="this.style.width = ((this.value.length + 2) * 8) + 'px';" required><br><br>
         <div class="text-danger" id="errorMessageForDelete" style="color: red;"></div><br>
         <button type="submit" class="btn btn-sm btn-primary mt-3 custom-btn">Delete</button>
     </form>
     <br>

   </div>
</template>

<script>
export default{
       data(){
           return{
               id:"",
               errorMessageForDelete:""
           };
       },
       methods:{
          async deleteTask(){
              let response = await fetch("http://localhost:8000/DeleteTaskDetail/", {
                method:'POST',
                credentials: "include",
                headers: {
                     'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                      deleteid: this.id
                })
              });
              console.log("emit event...")
              //this.$emit("task-detail-deleted");

              console.log(response.status)

              if(response.status!=200){
                 //errorMessageForDelete = 'Invalid task ID. Please enter a valid ID.';
                 document.getElementById("errorMessageForDelete").innerHTML = 'Invalid task ID. Please enter a valid ID.';
                 return;
              }

              else{

                document.getElementById("errorMessageForDelete").innerHTML = '';

              }

              let data= await response.json()

              const start = performance.now();

              document.getElementById(data.task_detail[0].id).innerHTML = ``;

              const end = performance.now();

              console.log(`DOM fetching time took ${end - start} milliseconds.`);

          }

       }

};
</script>

<style scope>

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

</style>