package com.tryScala

import org.apache.spark.sql.SparkSession

object  mapTest{
  val path= "Z:/Coursera-lectures/BD_UCSD/big-data-3/spark-wordcount/words.txt"
  def main(args: Array[String]) = {
    val spark = SparkSession.builder.appName("mapExample").master("local").getOrCreate()
    val data = spark.read.textFile(path).rdd
    val mapFile = data.map(line => (line,line.length)).filter(value => value=="cool")
  //  mapFile.foreach(println)

  //val flatmapFile = data.flatMap(lines => lines.split(" "))
   // flatmapFile.foreach(println)


    println(mapFile.count())
}



}