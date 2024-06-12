//These are the necessary components that are imported from the vue
import { createApp } from 'vue'
import {createRouter, createWebHistory} from "vue-router";

//This is where the css is imported from the file called style.css in same directory
import './style.css'

//These are where all the svelte files are imported
import App from './App.vue'
import mainPage from './components/mainPage.vue'
import RetrieveCalorieHistory from './components/RetrieveCalorieHistory.vue'
import UpdateTask from './components/UpdateTask.vue'
import CalorieTracker from './components/CalorieTracker.vue'
import FetchingExercisingVideos from './components/FetchingExercisingVideos.vue'
import automatedTesting from './components/automatedTesting.vue'

//This is where all the URL path to vue files are mapped
const router = createRouter({
    //The URL path to vue files mapping are stored in the web browser.
    history:createWebHistory(),
    routes:[
       {path: '/mainPage', name: 'mainPage', component: mainPage },
       {path: '/caloriehistory', name: 'RetrieveCalorieHistory', component: RetrieveCalorieHistory},
       {path: '/CalorieTracker', name: 'CalorieTracker', component: CalorieTracker},
       {path: '/updateTask/:id', name: 'UpdateTask', component: UpdateTask},
       {path: '/FetchingExercisingVideos', name: 'FetchingExercisingVideos', component: FetchingExercisingVideos},
       {path: '/automatedTesting', name: 'automatedTesting', component: automatedTesting},
    ],
});


//This makes the URL path to vue files mapping to be included in the website
createApp(App).use(router).mount('#app');
