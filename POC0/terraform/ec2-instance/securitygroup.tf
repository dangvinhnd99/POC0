resource "aws_security_group" "vinh_secuity" {
    name = "vinh_security_terraform"

    #incoming traffic
    ingress {
      cidr_blocks = var.cidr_blocks
      description = "allow ssh traffic"
      from_port = 22
      protocol = "tcp"
      to_port = 22
    }
    
    ingress {
        cidr_blocks = var.cidr_blocks
        description = "allow ... traffic"
        from_port = 8080
        protocol = "tcp"
        to_port = 8080
    }
    
    ingress {
        cidr_blocks = var.cidr_blocks
        description = "allow ... traffic"
        from_port = 80
        protocol = "tcp"
        to_port = 80
    }

    #outcoming traffic
    egress {
      cidr_blocks = var.cidr_blocks
      description = "allow ... traffic"
      from_port = 0
      protocol = "-1"
      to_port = 0
    } 
}