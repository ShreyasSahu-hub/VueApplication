<template class="p-3 mb-2 bg-light text-dark">

   <NavBar/> <!--Importing the HTML elements from the NavBar.vue file and execute it.-->

   <div class="top-container">
   <br><button @click="fetchCalorieDetails();" class="btn btn-sm btn-primary mt-3 custom-btn">Fetch all the calorie consumption details at all the dates</button><br><br>
   </div>

   <div class="bg-light text-dark rounded shadow-sm">

   <div id="content"></div>  <!--This is the placeholder for the displaying the amount of calories that the user consumes and at which date.-->

   </div>

</template>

<script>
import NavBar from '../components/NavBar.vue';
export default{
   components:{
      NavBar,
   },
   data(){
      //This is the caloriedetail variable created to store the calorie content of the user's food item and the date it has been consumed.
      return{
       caloriedetail:[],
      }

   },

   methods:{



     //This javascript function is used to fetch all the calories consumption history from the database via Django endpoint URL.

     async fetchCalorieDetails(){



        //The python function which is mapped to this Django endpoint URL is called in the view.py file and its code is executed.
        //The mapping is defined in the urls.py file in the protocolApplication.
        //The python function is called CalorieDetailRetrieved and credentials field stores the include value that remembers the user.
        //This will retrieve the calorie intake details that belongs to the user who is currently logged.
        //The Django endpoint URL is called by the GET http request method, which is used to fetch data, which is calorie intake detail.
        //Whatever the calorie intake details are fetched will be stored in the response variable.

        let response = await fetch("http://localhost:8000/RetrieveCalorieDetails/", {
              method: 'GET',
              credentials: "include"
        })



        //The calorie intake details are converted to a JSON format, so it will readable and easier to display that detail.
        let data = await response.json()



        this.caloriedetail = data.calorie_detail_retrieved;            //The variable called caloriedetail stores the calorie intake details.

        console.log(data)

        document.getElementById("content")



        //The HTMl tag elements are used to display the calorie consumption details and it will be stored in the div tag with the id called content.
        //In that way the placeholder that was explained earlier will execute the HTML tag elements to display the necessary details.
        //Here it stores the table header title.

        document.getElementById("content").innerHTML = `
        <h3>This table shows the amount of calories that you consumed at each date</h3>
        <table class="table">
           <tr>
             <th>Amount of calories consumed</th>
             <th>The date the calories has been consumed</th>
           </tr>
           <tbody>
           </tbody>
        </table>
        <br>
        <br>
        <h3>This table shows the total amount of calories at each month</h3>
        <table class="table">
           <tr>
             <th>Month</th>
             <th>Total calorie consumption</th>
           </tr>
           <tbody id="totalCalorie">
           </tbody>
        </table>
        `;

        const calorieSummary = {};

        //Each calorie intake details are iterated using the forEach built-in function, in order to display the content in a table row by row.

        data.calorie_detail_retrieved.forEach(calorie => {



            //The date at which the user consumes the food item is converted to UK date format in terms of  day/month/year and time (hours:minutes:seconds).

            const date = new Date(calorie.currentdate);

            const day = String(date.getUTCDate()).padStart(2, '0');
            const month = date.toLocaleString('default', { month: 'long' }); // Months are zero-based
            const year = date.getUTCFullYear();

            // Extract the time components
            const hours = String(date.getUTCHours()).padStart(2, '0');
            const minutes = String(date.getUTCMinutes()).padStart(2, '0');
            const seconds = String(date.getUTCSeconds()).padStart(2, '0');

            // Format the date in DD/MM/YYYY format
            const ukDateFormat = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;

            const dateString = `month: ${month}   year: ${year}`;

            if (calorieSummary[dateString]) {
                 calorieSummary[dateString] += calorie.amountofcalories;
            } else {
                 calorieSummary[dateString] = calorie.amountofcalories;
            }

            //Each calorie intake detail are displayed inside the HTML tag elements and it will be stored in the tbody tag.
            //This is a table body tag used to display the content of the table below the table header.
            //Here is where the calorie consumption details are displayed in table rows where each content are displayed in a table box.

            document.querySelector('tbody').innerHTML += `

                  <tr>
                    <td>${calorie.amountofcalories} Kcal</td>
                    <td>${ukDateFormat}</td>
                  </tr>
            `;

        });

        Object.keys(calorieSummary).forEach(date => {
            document.getElementById('totalCalorie').innerHTML += `
                <tr>
                    <td>${date}</td>
                    <td>${calorieSummary[date]} Kcal</td>
                </tr>
            `;
        });

     }

   }

}

</script>

<style>

.top-container {
       top:11%;
       left:35%;
}

</style>