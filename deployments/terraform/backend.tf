terraform {
  backend "gcs" {
    bucket  = "janashj-bucket-1234"
    prefix  = "qa/hello-world"
    project = "crested-acumen-315805"
  }
}
