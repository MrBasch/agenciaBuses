<template>
  <v-app>
    <Navbar/>
    <v-main class="main">
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  name: 'DefaultLayout',
  components:{
        Navbar,
    },
  data () {
    return {
      clipped: false,
    }
  }
}
</script>
<style>
.header_{
  display: flex;
  justify-content: space-between;

}
.theme--dark.v-application {
    background: whitesmoke;
    color: #021C36;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  background: #f4f4f4;
}
a {
  color: #666;
  text-decoration: none;
}
ul {
  list-style: none;
}

</style>
