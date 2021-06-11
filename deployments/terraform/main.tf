module "helm_deploy" {
  source                    = "fuchicorp/chart/helm"
  deployment_name           = "${var.deployment_name}"
  deployment_environment    = "${var.deployment_environment}"
  deployment_endpoint       = "${lookup(var.deployment_endpoint, "${var.deployment_environment}")}.${var.google_domain_name}"
  deployment_path           = "hello-world"     
  template_custom_vars = {
    deployment_image        = "${var.deployment_image}"
  }          
}


variable "deployment_name" {
    default = "hello-world"
    description = "- (Optional) The name of the deployment."
}
variable "deployment_environment" {
    default = "dev"
    description = "- (Optional) The name of the deployment."
}
variable "deployment_endpoint" {
    type = "map"
    default = {
        dev     = "dev.hello"
        qa      = "qa.hello"
        prod    = "hello"
        stage   = "stage.hello"
    }
    description = "- (Optional) The endpooint of the deployment."
}
variable "google_domain_name" {
  default = "janarasjorobaevas.net"
}

variable "deployment_image" {
    default = "docker.janarasjorobaevas.net/hello-world-two-stage:d3ce993"
    description = "- (Optional) The docker image of the deployment."
}

