<template>
  <v-dialog max-width="500px" v-model="open">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add Route</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter name"></v-text-field>
        <v-text-field v-model="code" label="Enter code"></v-text-field>
        <v-select
          multiple
          v-model="stations_selected"
          :items="stations"
          label="Select stations"
        ></v-select>
        <v-select
          v-model="state"
          :items="status"
          label="Select A Status"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            saveRoute(
              (code = code),
              (name = name),
              (list_stations = stations_selected),
              (state = state)
            )
          "
          color="green"
          >Add</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "createRouteModal",
  props: ["open"],
  data() {
    return {
      name: "",
      code: "",
      state: "",
      stations_selected: [],
      stations: [],
      routes: [],
      status: ["AVAILABLE", "CLOSED", "UNAVAILABLE"],
    };
  },
  methods: {
    async saveRoute(name, code, list_stations, state) {
      console.log(
        "code = ",
        code,
        "name =",
        name,
        "list_stations = ",
        list_stations,
        "state = ",
        state
      );
      await fetch(
        `http://127.0.0.1:8000/back/route?code=${code}&route=${code_route}&start_time=${start_time}&end_time=${end_time}&rut_driver=${rut_driver},&code_bus=${code_bus}`,
        {
          method: "POST",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
    },
    async getStations() {
      await fetch("http://127.0.0.1:8000/back/station", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((station) => this.stations.push(station.name));
        })
      );
    },
  },
  created() {
    this.getStations();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
</style>