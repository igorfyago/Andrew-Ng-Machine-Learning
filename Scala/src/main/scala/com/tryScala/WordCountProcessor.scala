package com.tryScala

import org.apache.spark._
import org.apache.spark.rdd.RDD

class WordCountProcessor {
  //methods have been moved to a class to unit test it
  def getWordsByLine(wordsByLine: RDD[String]): RDD[(String)] = {
    wordsByLine.flatMap(line => line.toUpperCase().split(" "))

    /*val counts = wordsByLine.flatMap(line => line.split(" "))
      .map(word => (word, 1))
      .reduceByKey(_ + _)*/

  }
}

object WordCount {
  val path= "Z:/Coursera-lectures/BD_UCSD/big-data-3/spark-wordcount/words.txt"
  System.setProperty("hadoop.home.dir", "D:\\spark-2.3.1-bin-hadoop2.7\\winutils");
  val conf = new SparkConf().setAppName("wordCount").setMaster("local")
  // Create a Scala Spark Context.
  val sc = new SparkContext(conf)

  /**
    * Main method is for counting word using spark submit
    */
  def main(args: Array[String]): Unit = {

    //val textFile = sc.textFile("hdfs:///user/cloudera/words.txt")
    val textFile = sc.textFile(path)
    val counts = textFile.flatMap(line => line.split(" "))
      .map(word => (word, 1))
      .reduceByKey(_ + _)

    //counts.saveAsTextFile("hdfs:///user/cloudera/spark_output/wordscount")
    counts.saveAsTextFile("Z:/Coursera-lectures/BD_UCSD/big-data-3/spark-wordcount/words_counted")
    println("====> ")
    counts.collect().sorted.foreach(println)
  }

}