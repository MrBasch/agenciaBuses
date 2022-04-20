<template>
  <div class="header_">
    <h1>Route id : {{ id }}</h1>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: `Route ${this.id}`,
    };
  },
  data() {
    return {
      id: this.$route.params.id,
      route: [],
    };
  },
  methods: {
    async getDetailRoute() {
      await fetch(
        `http://127.0.0.1:8000/back/detail_route?route_code=${this.id}`,
        {
          method: "GET",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
          cache: "default",
        }
      ).then((res) =>
        res.json().then((data) => {
          console.log("data fetch=", data);
          console.log("route = ", data.route);
          console.log("buses_list= ", data.selling_buses_places);
        })
      );
    },
  },
  created() {
    this.getDetailRoute();
  },
};
</script>

<style>
</style>