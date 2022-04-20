<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create station</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter station name"></v-text-field>
        <v-text-field v-model="code" label="Enter station code"></v-text-field>
        <v-text-field
          v-model="new_code"
          label="Enter station new_code"
        ></v-text-field>
        <v-select
          v-model="city"
          :items="cities"
          label="Select a city"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            updateStation((name = name), (code = code), (city_id = city.id))
          "
          color="#417D7A"
          >Add</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "updateStationModal",
  props: ["edit"],
  data() {
    return {
      code: "",
      new_code: "",
      name: "",
      cities: [],
      city: "",
    };
  },
  methods: {
    async updateStation(name, code, new_code, city_id) {
      await fetch(
        `http://127.0.0.1:8000/back/station?code=${code}&name=${name}&new_code=${new_code}&city_id=${city_id}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
    },
    async getCities() {
      await fetch("http://127.0.0.1:8000/back/city", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((city) => this.cities.push(city.name));
        })
      );
    },
  },
  created() {
    this.getCities();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
.cardTitle {
  background-color: #1a3c40;
}
</style>