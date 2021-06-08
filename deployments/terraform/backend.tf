terraform {
  backend "gcs" {
    bucket  = "janashj-bucket-1234"
    prefix  = "dev/hello-world"
    project = "crested-acumen-315805"
  }
}
