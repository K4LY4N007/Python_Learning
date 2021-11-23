import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
        backgroundColor: Colors.blueAccent,
        appBar: AppBar(
          title: const Center(child: Text('I AM POOR')),
          backgroundColor: Colors.blueGrey[900],
        ),
        body: const Center(
          child: Image(
            image: AssetImage('images/poor.jpg'),
          ),
        )),
  ));
}
