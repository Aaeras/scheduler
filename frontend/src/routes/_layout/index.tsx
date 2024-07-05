import { createFileRoute } from "@tanstack/react-router"

import Calendar from "@/components/calendar"
import useAuth from "../../hooks/useAuth"
import { Card } from "@/components/ui/card"

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
})

function Dashboard() {
  const { user: currentUser } = useAuth()

  return (
    <>
      <div className="max-w-fit mx-auto">
        <Card className="overflow-hidden h-screen">
          <Calendar />
        </Card>
      </div>
    </>
  )
}
