<template>

   <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
   </head>

   <NavBar/>

   <!--This is the button to click to execute the automated testing-->

   <div class="col-12">
   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
     <form method="POST" enctype="multiple/form-data" v-on:submit.prevent="tests();">

         <button class="btn btn-primary btn-lg full-width-form" size="100" type="submit">Test the web app</button>

     </form>
   </div>
   </div>

</template>

<script>
import NavBar from '../components/NavBar.vue';
export default{

    components:{

        NavBar,

    },
    methods:{

            async tests(){


               //The specified Django URL endpoint is fetched using the GET http method.
               //The credentials have a field that stores a include value, which will remember which user is logged in.

               let response = await fetch("http://localhost:8000/test_results/",{

                        method: 'GET',
                        credentials: "include"

               })

               var testResults = await response.json()

               console.log(testResults.test_results[0])

            }

    }

}

</script>

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

</style>